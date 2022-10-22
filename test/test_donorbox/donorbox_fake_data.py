campaign_1_json = {
    'created_at': '2022-09-20T18:47:05.381Z',
    'currency': 'usd',
    'donations_count': 0,
    'formatted_goal_amount': '$1,000',
    'formatted_total_raised': '$0',
    'goal_amt': '1000.0',
    'id': 366172,
    'name': 'Test Campaign',
    'slug': 'test-campaign-623',
    'total_raised': '0.0',
    'updated_at': '2022-09-21T05:38:28.915Z'
}

campaign_2_json = {
    'id': 366590, 
    'name': 'Membership Campaign', 
    'slug': 'membership-campaign-10', 
    'currency': 'usd', 
    'created_at': '2022-09-21T21:05:04.909Z', 
    'updated_at': '2022-10-19T05:39:20.993Z', 
    'goal_amt': '0.0', 
    'formatted_goal_amount': '$0', 
    'total_raised': '0.0', 
    'formatted_total_raised': '$0', 
    'donations_count': 0
}

get_campaigns_response_json = [campaign_1_json]

get_campaigns_filtered_response_json = [campaign_2_json]

get_campaigns_desc_order = [campaign_2_json, campaign_1_json]

get_campaigns_asc_order = [campaign_1_json, campaign_2_json]

donation_1_json = {
    'campaign': { 'id': 366172, 'name': 'Test Campaign', 'started_at': '2022-09-20T18:47:05.381Z' }, 
    'donor': {
            'id': 7508840, 'name': 'Megan Rapinoe', 'first_name': 'Megan', 'last_name': 'Rapinoe', 
            'email': 'fakeemail@email.com', 'phone': None, 'address': None, 'city': None, 'state': None, 
            'zip_code': None, 'country': None, 'employer': None, 'occupation': None
            }, 
    'amount': '3.0', 'formatted_amount': '$3', 'converted_amount': '3.0', 'formatted_converted_amount': '$3', 
    'converted_net_amount': '2.57', 'formatted_converted_net_amount': '$2.57', 'recurring': True, 
    'first_recurring_donation': True, 'amount_refunded': '0.0', 'formatted_amount_refunded': '', 
    'stripe_charge_id': 'ABCDEFG123132', 'id': 25497167, 'status': 'paid', 'donation_type': 'stripe', 
    'donation_date': '2022-10-19T17:32:52.613Z', 'anonymous_donation': False, 'gift_aid': False, 
    'designation': None, 'join_mailing_list': False, 'comment': 'testing testing', 'donating_company': None, 
    'currency': 'USD', 'converted_currency': 'USD', 'utm_campaign': None,  'utm_source': None, 'utm_medium': None,
    'utm_term': None, 'utm_content': None, 'processing_fee': 0.39, 'formatted_processing_fee': '$0.39', 
    'fee_covered': False, 'questions': [], 'plan_id': 1173773, 'interval': '1 M'
}

donation_2_json = {
    'campaign': {'id': 366172, 'name': 'Test Campaign', 'started_at': '2022-09-20T18:47:05.381Z'}, 
    'donor': {
        'id': 7509137, 'name': 'Crystal Dunn', 'first_name': 'Crystal', 'last_name': 'Dunn', 
        'email': 'fake2mail2@gmail.com', 'phone': None, 'address': None, 'city': None, 'state': None, 
        'zip_code': None, 'country': None, 'employer': None, 'occupation': None
    }, 
    'amount': '4.0', 'formatted_amount': '$4', 'converted_amount': '4.0', 'formatted_converted_amount': '$4', 
    'converted_net_amount': '3.52', 'formatted_converted_net_amount': '$3.52', 'recurring': True, 
    'first_recurring_donation': True, 'amount_refunded': '0.0', 'formatted_amount_refunded': '', 
    'stripe_charge_id': '31231213123ASAD', 'id': 25497700, 'status': 'paid', 'donation_type': 'stripe', 
    'donation_date': '2022-10-19T18:19:06.044Z', 'anonymous_donation': False, 'gift_aid': False, 
    'designation': None, 'join_mailing_list': False, 'comment': 'bleep bloop', 'donating_company': None, 
    'currency': 'USD', 'converted_currency': 'USD', 'utm_campaign': None, 'utm_source': None, 
    'utm_medium': None, 'utm_term': None, 'utm_content': None, 'processing_fee': 0.42, 
    'formatted_processing_fee': '$0.42', 'fee_covered': False, 'questions': [], 'plan_id': 1173856, 
    'interval': '1 M'
}

donation_3_json = {
    'campaign': {'id': 366172, 'name': 'Test Campaign', 'started_at': '2022-09-20T18:47:05.381Z'}, 
    'donor': {
        'id': 7508840, 'name': 'Rose Lavelle', 'first_name': 'Rose', 'last_name': 'Lavelle', 
        'email': 'fake@fakeemail.com', 'phone': None, 'address': None, 'city': None, 'state': None, 
        'zip_code': None, 'country': None, 'employer': None, 'occupation': None
    }, 
    'amount': '3.0', 'formatted_amount': '$3', 'converted_amount': '3.0', 'formatted_converted_amount': '$3',
    'converted_net_amount': '2.57', 'formatted_converted_net_amount': '$2.57', 'recurring': True, 
    'first_recurring_donation': True, 'amount_refunded': '0.0', 'formatted_amount_refunded': '', 
    'stripe_charge_id': '123ABC123ABC', 'id': 25525370, 'status': 'paid', 
    'donation_type': 'stripe', 'donation_date': '2022-10-20T19:33:31.744Z', 'anonymous_donation': False, 
    'gift_aid': False, 'designation': None, 'join_mailing_list': False, 'comment': None, 
    'donating_company': None, 'currency': 'USD', 'converted_currency': 'USD', 'utm_campaign': None, 
    'utm_source': None, 'utm_medium': None, 'utm_term': None, 'utm_content': None, 'processing_fee': 0.39, 
    'formatted_processing_fee': '$0.39', 'fee_covered': False, 'questions': [], 'plan_id': 1175651, 
    'interval': '1 M'
}


get_donations_response_json = [donation_3_json, donation_1_json, donation_2_json]

get_donations_amount_min_3 = [donation_3_json, donation_1_json, donation_2_json]
get_donations_amount_min_4 = [donation_2_json]
get_donations_amount_min_5 = []

get_donations_amount_max_3 = [donation_3_json, donation_1_json]
get_donations_amount_max_4 = [donation_3_json, donation_1_json, donation_2_json]
get_donations_amount_max_2 = []

get_donations_date_from_valid = []
get_donations_date_from_invalid = []