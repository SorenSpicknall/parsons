import os
import json
import logging

from parsons.etl.table import Table
from parsons.google.utitities import setup_google_application_credentials, hexavigesimal

import gspread
from google.oauth2.service_account import Credentials
from gspread.exceptions import APIError
from requests.exceptions import HTTPError, ReadTimeout
import time
import utilities

logger = logging.getLogger(__name__)


class GoogleSheets:
    """
    A connector for Google Sheets, handling data import and export.

    `Args:`
        google_keyfile_dict: dict
            A dictionary of Google Drive API credentials, parsed from JSON provided
            by the Google Developer Console. Required if env variable
            ``GOOGLE_DRIVE_CREDENTIALS`` is not populated.
        subject: string
            In order to use account impersonation, pass in the email address of the account to be
            impersonated as a string.
    """

    def __init__(self, google_keyfile_dict=None, subject=None):

        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive",
        ]

        setup_google_application_credentials(google_keyfile_dict, "GOOGLE_DRIVE_CREDENTIALS")
        google_credential_file = open(os.environ["GOOGLE_DRIVE_CREDENTIALS"])
        credentials_dict = json.load(google_credential_file)

        credentials = Credentials.from_service_account_info(
            credentials_dict, scopes=scope, subject=subject
        )

        self.gspread_client = gspread.authorize(credentials)

    def _get_worksheet(self, spreadsheet_id, worksheet=0):
        # Internal method to retrieve a worksheet object.

        # Check if the worksheet is an integer, if so find the sheet by index
        if isinstance(worksheet, int):
            return self.gspread_client.open_by_key(spreadsheet_id).get_worksheet(worksheet)

        elif isinstance(worksheet, str):
            idx = self.list_worksheets(spreadsheet_id).index(worksheet)
            try:
                return self.gspread_client.open_by_key(spreadsheet_id).get_worksheet(idx)
            except:  # noqa: E722
                raise ValueError(f"Couldn't find worksheet {worksheet}")

        else:
            raise ValueError(f"Couldn't find worksheet index or title {worksheet}")

    def list_worksheets(self, spreadsheet_id):
        """
        Return a list of worksheets in the spreadsheet.

        `Args:`
            spreadsheet_id: str
                The ID of the spreadsheet (Tip: Get this from the spreadsheet URL)
        `Returns:`
            list
                A List of worksheets order by their index
        """
        worksheets = self.gspread_client.open_by_key(spreadsheet_id).worksheets()
        return [w.title for w in worksheets]

    def get_worksheet_index(self, spreadsheet_id, title):
        """
        Get the first sheet in a Google spreadsheet with the given title. The
        title is case sensitive and the index begins with 0.

        `Args:`
            spreadsheet_id: str
                The ID of the spreadsheet (Tip: Get this from the spreadsheet URL)
            title: str
                The sheet title
        `Returns:`
            str
                The sheet index
        """

        sheets = self.gspread_client.open_by_key(spreadsheet_id).worksheets()
        for index, sheet in enumerate(sheets):
            if sheet.title == title:
                return index
        raise ValueError(f"Couldn't find sheet with title {title}")

    def get_worksheet(self, spreadsheet_id, worksheet=0):
        """
        Create a ``parsons table`` from a sheet in a Google spreadsheet, given the sheet index.

        `Args:`
            spreadsheet_id: str
                The ID of the spreadsheet (Tip: Get this from the spreadsheet URL)
            worksheet: str or int
                The index or the title of the worksheet. The index begins with
                0.
        `Returns:`
            Parsons Table
                See :ref:`parsons-table` for output options.
        """

        worksheet = self._get_worksheet(spreadsheet_id, worksheet)
        tbl = Table(worksheet.get_all_values())
        logger.info(f"Retrieved worksheet with {tbl.num_rows} rows.")
        return tbl

    def share_spreadsheet(
        self,
        spreadsheet_id,
        sharee,
        share_type="user",
        role="reader",
        notify=True,
        notify_message=None,
        with_link=False,
    ):
        """
        Share a spreadsheet with a user, group of users, domain and/or the public.

        `Args:`
            spreadsheet_id: str
                The ID of the spreadsheet (Tip: Get this from the spreadsheet URL)
            sharee: str
                User or group e-mail address, domain name to share the spreadsheet
                with. To share publicly, set sharee value to ``None``.
            share_type: str
                The sharee type. Allowed values are: ``user``, ``group``, ``domain``,
                ``anyone``.
            role: str
                The primary role for this user. Allowed values are: ``owner``,
                ``writer``, ``reader``.
            notify: boolean
                Whether to send an email to the target user/domain.
            email_message: str
                The email to be sent if notify kwarg set to True.
            with_link: boolean
                Whether a link is required for this permission.
        """

        spreadsheet = self.gspread_client.open_by_key(spreadsheet_id)
        spreadsheet.share(
            sharee,
            share_type,
            role,
            notify=notify,
            email_message=notify_message,
            with_link=with_link,
        )
        logger.info(f"Shared spreadsheet {spreadsheet_id}.")

    def get_spreadsheet_permissions(self, spreadsheet_id):
        """
        List the permissioned users and groups for a spreadsheet.

        `Args:`
            spreadsheet_id: str
                The ID of the spreadsheet (Tip: Get this from the spreadsheet URL)
        `Returns:`
            Parsons Table
                See :ref:`parsons-table` for output options.
        """

        spreadsheet = self.gspread_client.open_by_key(spreadsheet_id)
        tbl = Table(spreadsheet.list_permissions())
        logger.info(f"Retrieved permissions for {spreadsheet_id} spreadsheet.")
        return tbl

    def create_spreadsheet(self, title, editor_email=None, folder_id=None):
        """
        Creates a new Google spreadsheet. Optionally shares the new doc with
        the given email address. Optionally creates the sheet in a specified folder.

        `Args:`
            title: str
                The human-readable title of the new spreadsheet
            editor_email: str (optional)
                Email address which should be given permissions on this spreadsheet.
                Tip: You may want to share this file with the service account.
            folder_id: str (optional)
                ID of the Google folder where the spreadsheet should be created.
                Tip: Get this from the folder URL.
                Anyone shared on the folder will have access to the spreadsheet.

        `Returns:`
            str
                The spreadsheet ID
        """

        spreadsheet = self.gspread_client.create(title, folder_id=folder_id)

        if editor_email:
            self.gspread_client.insert_permission(
                spreadsheet.id,
                editor_email,
                perm_type="user",
                role="writer",
            )

        logger.info(f"Created spreadsheet {spreadsheet.id}")
        return spreadsheet.id

    def delete_spreadsheet(self, spreadsheet_id):
        """
        Deletes a Google spreadsheet.

        `Args:`
            spreadsheet_id: str
                The ID of the spreadsheet (Tip: Get this from the spreadsheet URL)
        """
        self.gspread_client.del_spreadsheet(spreadsheet_id)
        logger.info(f"Deleted spreadsheet {spreadsheet_id}")

    def add_sheet(self, spreadsheet_id, title=None, rows=100, cols=25):
        """
        Adds a sheet to a Google spreadsheet.

        `Args:`
            spreadsheet_id: str
                The ID of the spreadsheet (Tip: Get this from the spreadsheet URL)
            rows: int
                Number of rows
            cols
                Number of cols

        `Returns:`
            str
                The sheet index
        """
        spreadsheet = self.gspread_client.open_by_key(spreadsheet_id)
        spreadsheet.add_worksheet(title, rows, cols)
        sheet_count = len(spreadsheet.worksheets())
        logger.info("Created worksheet.")
        return sheet_count - 1

    def append_to_sheet(
        self, spreadsheet_id, table, worksheet=0, user_entered_value=False, **kwargs
    ):
        """
        Append data from a Parsons table to a Google sheet. Note that the table's columns are
        ignored, as we'll be keeping whatever header row already exists in the Google sheet.

        `Args:`
            spreadsheet_id: str
                The ID of the spreadsheet (Tip: Get this from the spreadsheet URL)
            table: obj
                Parsons table
            worksheet: str or int
                The index or the title of the worksheet. The index begins with
                0.
            user_entered_value: bool (optional)
                If True, will submit cell values as entered (required for entering formulas).
                Otherwise, values will be entered as strings or numbers only.
        """

        # This is in here to ensure backwards compatibility with previous versions of Parsons.
        if "sheet_index" in kwargs:
            worksheet = kwargs["sheet_index"]
            logger.warning("Argument deprecated. Use worksheet instead.")

        sheet = self._get_worksheet(spreadsheet_id, worksheet)

        # Grab the existing data, so we can figure out where to start adding new data as a batch.
        # TODO Figure out a way to do a batch append without having to read the whole sheet first.
        # Maybe use gspread's low-level batch_update().
        existing_table = self.get_worksheet(spreadsheet_id, worksheet)

        # If the existing sheet is blank, then just overwrite the table.
        if existing_table.num_rows == 0:
            return self.overwrite_sheet(spreadsheet_id, table, worksheet, user_entered_value)

        cells = []
        for row_num, row in enumerate(table.data):
            for col_num, cell in enumerate(row):
                # Add 2 to allow for the header row, and for google sheets indexing starting at 1
                sheet_row_num = existing_table.num_rows + row_num + 2
                cells.append(gspread.Cell(sheet_row_num, col_num + 1, row[col_num]))

        value_input_option = "RAW"
        if user_entered_value:
            value_input_option = "USER_ENTERED"

        # Update the data in one batch
        sheet.update_cells(cells, value_input_option=value_input_option)
        logger.info(f"Appended {table.num_rows} rows to worksheet.")

    def paste_data_in_sheet(
        self, spreadsheet_id, table, worksheet=0, header=True, startrow=0, startcol=0
    ):
        """
        Pastes data from a Parsons table to a Google sheet. Note that this may overwrite
        presently existing data. This function is useful for adding data to a subsection
        if an existint sheet that will have other existing data - constrast to
        `overwrite_sheet` (which will fully replace any existing data) and `append_to_sheet`
        (whuch sticks the data only after all other existing data).

        `Args:`
            spreadsheet_id: str
                The ID of the spreadsheet (Tip: Get this from the spreadsheet URL).
            table: obj
                Parsons table
            worksheet: str or int
                The index or the title of the worksheet. The index begins with 0.
            header: bool
                Whether or not the header row gets pasted with the data.
            startrow: int
                Starting row position of pasted data. Counts from 0.
            startcol: int
                Starting column position of pasted data. Counts from 0.
        """
        sheet = self._get_worksheet(spreadsheet_id, worksheet)

        number_of_columns = len(table.columns)
        number_of_rows = table.num_rows + 1 if header else table.num_rows

        if not number_of_rows or not number_of_columns:  # No data to paste
            logger.warning(
                f"No data available to paste, table size "
                f"({number_of_rows}, {number_of_columns}). Skipping."
            )
            return

        # gspread uses ranges like "C3:J7", so we need to convert to this format
        data_range = (
            hexavigesimal(startcol + 1)
            + str(startrow + 1)
            + ":"
            + hexavigesimal(startcol + number_of_columns)
            + str(startrow + number_of_rows)
        )

        # Unpack data. Hopefully this is small enough for memory
        data = [[]] * table.num_rows
        for row_num, row in enumerate(table.data):
            data[row_num] = list(row)

        if header:
            sheet.update(data_range, [table.columns] + data)
        else:
            sheet.update(data_range, data)

        logger.info(f"Pasted data to {data_range} in worksheet.")

    def overwrite_sheet(
        self, spreadsheet_id, table, worksheet=0, user_entered_value=False, **kwargs
    ):
        """
        Replace the data in a Google sheet with a Parsons table, using the table's columns as the
        first row.

        `Args:`
            spreadsheet_id: str
                The ID of the spreadsheet (Tip: Get this from the spreadsheet URL)
            table: obj
                Parsons table
            worksheet: str or int
                The index or the title of the worksheet. The index begins with
                0.
            user_entered_value: bool (optional)
                If True, will submit cell values as entered (required for entering formulas).
                Otherwise, values will be entered as strings or numbers only.
        """

        # This is in here to ensure backwards compatibility with previous versions of Parsons.
        if "sheet_index" in kwargs:
            worksheet = kwargs["sheet_index"]
            logger.warning("Argument deprecated. Use worksheet instead.")

        sheet = self._get_worksheet(spreadsheet_id, worksheet)
        sheet.clear()

        value_input_option = "RAW"
        if user_entered_value:
            value_input_option = "USER_ENTERED"

        # Add header row
        sheet.append_row(table.columns, value_input_option=value_input_option)

        cells = []
        for row_num, row in enumerate(table.data):
            for col_num, cell in enumerate(row):
                # We start at row #2 to keep room for the header row we added above
                cells.append(gspread.Cell(row_num + 2, col_num + 1, row[col_num]))

        # Update the data in one batch
        sheet.update_cells(cells, value_input_option=value_input_option)
        logger.info("Overwrote worksheet.")

    def format_cells(self, spreadsheet_id, range, cell_format, worksheet=0):
        """
        Format the cells of a worksheet.

        `Args:`
            spreadsheet_id: str
                The ID of the spreadsheet (Tip: Get this from the spreadsheet URL)
            range: str
                The cell range to format. E.g. ``"A2"`` or ``"A2:B100"``
            cell_format: dict
                The formatting to apply to the range. Full options are specified in
                the GoogleSheets `API documentation <https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/cells#cellformat>`_.
            worksheet: str or int
                The index or the title of the worksheet. The index begins with
                0.

        **Examples**

        .. code-block:: python

            # Set 'A4' cell's text format to bold
            gs.format_cells(sheet_id, "A4", {"textFormat": {"bold": True}}, worksheet=0)

            # Color the background of 'A2:B2' cell range yellow,
            # change horizontal alignment, text color and font size
            gs.format_cells.format(sheet_id, "A2:B2", {
                "backgroundColor": {
                    "red": 0.0,
                    "green": 0.0,
                    "blue": 0.0
                    },
                "horizontalAlignment": "CENTER",
                "textFormat": {
                    "foregroundColor": {
                        "red": 1.0,
                        "green": 1.0,
                        "blue": 0.0
                        },
                        "fontSize": 12,
                        "bold": True
                        }
                    }, worksheet=0)

        """  # noqa: E501,E261

        ws = self._get_worksheet(spreadsheet_id, worksheet)
        ws.format(range, cell_format)
        logger.info("Formatted worksheet")

    def attempt_gsheet_method(self, method, i=1, max=6, wait_time=15, **kwargs):
        """
        The Google Sheets API has notoriously strict rate limits (e.g. 60 calls per minute). This
        function calls itself (i.e. is recursive) to help configure wait times and retry attempts
        needed to wait out rate limit errors instead of letting them derail a script.
        `Args:`
            method: str
                The name of the Parsons GoogleSheets method to be attempted
            i: int
                Where to start the retry count - defaults to 0; mostly needed for recursive calls
            max: int
                How many attempts to make before giving up - defaults to 4
            wait_time: int
                Number of seconds to wait between attempts - defaults to 15
            kwargs: dict
                Any arguments required by `method` - note that positional args will have to be named
        `Returns:`
            Whatever `method` is supposed to return

        """

        # Recursively account for nested methods as needed
        nested_methods = method.split(".")

        if len(nested_methods) == 1:
            final_method = self
        else:
            final_method = self[nested_methods[0]]
            nested_methods.pop(0)

        try:

            # If final_method isn't callable, then the API call is made in the loop, not below
            for m in nested_methods:
                final_method = getattr(final_method, m)

            # Using getattr allows the method/attribute to be user-provided
            if callable(final_method):
                output = final_method(**kwargs)
            else:
                output = final_method

        except (APIError, HTTPError, ReadTimeout, ConnectionError) as e:
            # Lets get the ordinals right, because why not
            if i % 10 == 1:
                ordinal = "st"
            elif i % 10 == 2:
                ordinal = "nd"
            else:
                ordinal = "th"

            logger.debug(f"trying to {method} for the {i}{ordinal} time")
            if i < max:
                time.sleep(wait_time)
                i += 1
                return self.attempt_gsheet_method(method, i, max, wait_time, **kwargs)

            else:
                raise e

        return output

    def combine_multiple_sheet_data(self, sheet_ids, worksheet_id=None):
        """
        Combines data from multiple Google Sheets into a Parsons Table.
        The spreadsheets will be treated as if they are concatenated, meaning columns would
        need to align positionally with matching data types.
        This function also adds a spreedsheet_id and spreadsheet_title
        columns to the resulting table.

        `Args:`
            sheet_ids: str, list
                The IDs of the Google Spreadsheets with that data to be combined. Can be a
                comma-separated string of IDs or a list.

            worksheet_id: str (optional)
                If None, the first worksheet (ID = 0) is assumed.

        `Returns:` obj
            Parsons Table containing the concatenated data from all the sheets.
        """
        id_col = "sheet_id"
        sheet_id_list = []

        # Parse different possible sheet_ids types
        if isinstance(sheet_ids, list):
            # Already a list!
            sheet_id_list = sheet_ids

        elif "," in sheet_ids:
            # Comma-separated string
            sheet_id_list = [x.strip() for x in sheet_ids.split(",")]

        else:
            raise ValueError(f"{sheet_ids} is not a valid string or list GSheet IDs")

        # Non-DB table options yield a list, convert to Parsons table with default worksheet col
        if sheet_id_list:
            sheet_id_tbl = [{"sheet_id": x, "worksheet_id": 0} for x in sheet_id_list]

        if not worksheet_id:
            worksheet_id = "worksheet_id"

        # Empty table to accumulate data from spreadsheets
        combined = Table()

        # Set for path to temp file to keep storage/memory in check for large lists
        temp_files = []

        logger.info(
            f"Found {sheet_id_tbl.num_rows} Spreadsheets. Looping to get data from each one."
        )

        for sheet_id in sheet_id_tbl:

            # Keep a lid on how many temp files result from materializing below
            if len(temp_files) > 1:
                utilities.files.close_temp_file(temp_files[0])
                temp_files.remove(temp_files[0])

            # Grab the sheet's data
            data = self.attempt_gsheet_method(
                "get_worksheet",
                max=10,
                wait_time=60,
                spreadsheet_id=sheet_id[id_col],
                worksheet=sheet_id[worksheet_id],
            )
            # Add the sheet ID as a column
            data.add_column("spreadsheet_id", sheet_id[id_col])

            # Retrieve sheet title (with attempts to handle rate limits) and add as a column
            self.__sheet_obj = self.gspread_client.open_by_key(sheet_id[id_col])
            sheet_title = str(self.attempt_gsheet_method("sheet_obj.title"))
            del self.__sheet_obj
            data.add_column("spreadsheet_title", sheet_title)

            # Accumulate and materialize
            combined.concat(data)
            temp_files.append(combined.materialize_to_file())
        return combined

    def read_sheet(self, spreadsheet_id, sheet_index=0):
        # Deprecated method v0.14 of Parsons.

        logger.warning("Deprecated method. Use get_worksheet() instead.")
        return self.get_worksheet(spreadsheet_id, sheet_index)

    def read_sheet_with_title(self, spreadsheet_id, title):
        # Deprecated method v0.14 of Parsons.

        logger.warning("Deprecated method. Use get_worksheet() instead.")
        return self.get_worksheet(spreadsheet_id, title)

    def get_sheet_index_with_title(self, spreadsheet_id, title):
        # Deprecated method v0.14 of Parsons.

        logger.warning("Deprecated method. Use get_worksheet_index   instead.")
        return self.get_worksheet_index(spreadsheet_id, title)
