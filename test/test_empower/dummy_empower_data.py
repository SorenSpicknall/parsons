dummy_data = {
    "success": True,
    "profiles": [
        {
            "eid": "1zpyd08a6w9ulq",
            "parentEid": "63nvsmpvx46870",
            "role": "campaignDirector",
            "firstName": "Bob",
            "lastName": "Loblaw",
            "email": "bob@gmail.com",
            "phone": None,
            "city": None,
            "state": None,
            "zip": None,
            "address": None,
            "address2": None,
            "vanId": None,
            "myCampaignVanId": None,
            "lastUsedEmpowerMts": 1696522334107,
            "notes": "",
            "regionId": 5125,
            "createdMts": 1695755343766,
            "updatedMts": None,
            "currentCtaId": 8311,
            "activeCtaIds": [8311],
        },
        {
            "eid": "frzst1fnprr6n2",
            "parentEid": "63nvsmpvx46870",
            "role": "campaignDirector",
            "firstName": "John",
            "lastName": "Smith",
            "email": "Jon@gmail.com",
            "phone": None,
            "city": None,
            "state": None,
            "zip": None,
            "address": None,
            "address2": None,
            "vanId": None,
            "myCampaignVanId": None,
            "lastUsedEmpowerMts": 1696626131104,
            "notes": "",
            "regionId": 5125,
            "createdMts": 1695755297395,
            "updatedMts": 1696011335276,
            "currentCtaId": 8311,
            "activeCtaIds": [8311],
        },
        {
            "eid": "63nvsmpvx46870",
            "parentEid": None,
            "role": "campaignDirector",
            "firstName": "Sally",
            "lastName": "Jones",
            "email": "sally@gmail.com",
            "phone": None,
            "city": None,
            "state": None,
            "zip": None,
            "address": None,
            "address2": None,
            "vanId": None,
            "myCampaignVanId": None,
            "lastUsedEmpowerMts": 1695755125095,
            "notes": "",
            "regionId": 5125,
            "createdMts": 1695752839622,
            "updatedMts": 1695753353687,
            "currentCtaId": 8311,
            "activeCtaIds": [8311],
        },
    ],
    "ctas": [
        {
            "id": 8156,
            "name": "Let's get started!",
            "description": "This is where...",
            "instructionsHtml": '<p>To get started...',
            "prompts": [
                {
                    "id": 16719,
                    "ctaId": 8156,
                    "promptText": "How do you want to volunteer?",
                    "vanId": None,
                    "isDeleted": False,
                    "answerInputType": "CHECKBOX",
                    "ordering": 1,
                    "dependsOnInitialDispositionResponse": None,
                    "answers": [
                        {
                            "id": 55950,
                            "promptId": 16719,
                            "answerText": "Attend Events",
                            "vanId": None,
                            "isDeleted": False,
                            "ordering": 1,
                        },
                        {
                            "id": 55951,
                            "promptId": 16719,
                            "answerText": "Talk to friends and family",
                            "vanId": None,
                            "isDeleted": False,
                            "ordering": 2,
                        },
                        {
                            "id": 55952,
                            "promptId": 16719,
                            "answerText": "Canvassing",
                            "vanId": None,
                            "isDeleted": False,
                            "ordering": 3,
                        },
                        {
                            "id": 55953,
                            "promptId": 16719,
                            "answerText": "Phone banking",
                            "vanId": None,
                            "isDeleted": False,
                            "ordering": 4,
                        },
                        {
                            "id": 55954,
                            "promptId": 16719,
                            "answerText": "Text banking",
                            "vanId": None,
                            "isDeleted": False,
                            "ordering": 5,
                        },
                        {
                            "id": 55955,
                            "promptId": 16719,
                            "answerText": "Other (specify in notes)",
                            "vanId": None,
                            "isDeleted": False,
                            "ordering": 6,
                        },
                    ],
                }
            ],
            "shareables": [],
            "createdMts": 1695752752987,
            "updatedMts": None,
            "organizationId": 1095,
            "regionIds": [5125],
            "recruitmentQuestionType": "invite",
            "recruitmentTrainingUrl": None,
            "prioritizations": [],
            "isIntroCta": True,
            "scheduledLaunchTimeMts": 1695752752987,
            "activeUntilMts": None,
            "shouldUseAdvancedTargeting": False,
            "advancedTargetingFilter": None,
            "defaultPriorityLabelKey": None,
            "actionType": "personal",
            "spokeCampaignId": None,
            "textCanvassingType": None,
            "turfCuttingType": None,
            "conversationStarter": None,
            "isPersonal": True,
            "isGeocodingDone": True,
            "customRecruitmentPromptText": None,
            "isBatchImportDone": True,
            "hasAssignableTurfs": False,
            "associatedElectionId": None,
            "shouldDisplayElectionDayPollingLocation": False,
            "shouldDisplayEarlyVotingPollingLocation": False,
            "shouldShowMatchButton": False,
            "questions": [
                {
                    "key": 1,
                    "type": "Normal",
                    "text": "How do you want to volunteer?",
                    "options": [
                        "Attend Events",
                        "Talk to friends and family",
                        "Canvassing",
                        "Phone banking",
                        "Text banking",
                        "Other (specify in notes)",
                    ],
                }
            ],
        },
        {
            "id": 8311,
            "name": "TEST",
            "description": "Please test this for us!",
            "instructionsHtml": "<p>Please load at least 25",
            "prompts": [],
            "shareables": [
                {
                    "type": "link",
                    "url": "http://bioinfo.uib.es/~joemiro/RecEscr/PoliticsandEngLang.pdf",
                    "displayLabel": "Leisure reading",
                }
            ],
            "createdMts": 1696624915388,
            "updatedMts": None,
            "organizationId": 1095,
            "regionIds": [5125],
            "recruitmentQuestionType": "training",
            "recruitmentTrainingUrl": "https://forms.gle/Q1YX66WWQq8VGHeV8",
            "prioritizations": [],
            "isIntroCta": False,
            "scheduledLaunchTimeMts": 1696624915388,
            "activeUntilMts": None,
            "shouldUseAdvancedTargeting": False,
            "advancedTargetingFilter": None,
            "defaultPriorityLabelKey": None,
            "actionType": "relational",
            "spokeCampaignId": None,
            "textCanvassingType": "manual",
            "turfCuttingType": None,
            "conversationStarter": "Hey {recipientname} -- it's {sendername}.",
            "isPersonal": False,
            "isGeocodingDone": True,
            "customRecruitmentPromptText": None,
            "isBatchImportDone": True,
            "hasAssignableTurfs": False,
            "associatedElectionId": None,
            "shouldDisplayElectionDayPollingLocation": False,
            "shouldDisplayEarlyVotingPollingLocation": False,
            "shouldShowMatchButton": False,
            "questions": [],
        },
    ],
    "ctaResults": [
        {
            "profileEid": "m48oukqkfxf6in",
            "ctaId": 8311,
            "contactedMts": 1696630492605,
            "answerIdsByPromptId": {},
            "notes": None,
            "answers": {},
        },
        {
            "profileEid": "mqms2mh3hhen5y",
            "ctaId": 8311,
            "contactedMts": 1696630502526,
            "answerIdsByPromptId": {},
            "notes": None,
            "answers": {},
        },
        {
            "profileEid": "eskhmei145adzx",
            "ctaId": 8311,
            "contactedMts": 1696630508282,
            "answerIdsByPromptId": {},
            "notes": None,
            "answers": {},
        },
        {
            "profileEid": "xdm0xtu62jsf29",
            "ctaId": 8311,
            "contactedMts": 1696630513369,
            "answerIdsByPromptId": {},
            "notes": None,
            "answers": {},
        },
        {
            "profileEid": "rciszn1qtuqxfj",
            "ctaId": 8311,
            "contactedMts": 1696630517176,
            "answerIdsByPromptId": {},
            "notes": None,
            "answers": {},
        },
        {
            "profileEid": "480opsrmfjzns4",
            "ctaId": 8311,
            "contactedMts": 1696630520827,
            "answerIdsByPromptId": {},
            "notes": None,
            "answers": {},
        },
        {
            "profileEid": "k6xgo161z4g6r2",
            "ctaId": 8311,
            "contactedMts": 1696628059352,
            "answerIdsByPromptId": {},
            "notes": None,
            "answers": {},
        },
        {
            "profileEid": "ndpgftmbzc3gn8",
            "ctaId": 8311,
            "contactedMts": 1696628061778,
            "answerIdsByPromptId": {},
            "notes": None,
            "answers": {},
        },
        {
            "profileEid": "yjg44ywsbfxfmq",
            "ctaId": 8311,
            "contactedMts": 1696628062789,
            "answerIdsByPromptId": {},
            "notes": None,
            "answers": {},
        },
        {
            "profileEid": "fj7qxof19e0e6c",
            "ctaId": 8311,
            "contactedMts": 1696628063833,
            "answerIdsByPromptId": {},
            "notes": None,
            "answers": {},
        },
        {
            "profileEid": "kncehygy5zvfru",
            "ctaId": 8311,
            "contactedMts": 1696628065465,
            "answerIdsByPromptId": {},
            "notes": None,
            "answers": {},
        },
    ],
    "regions": [
        {
            "id": 5125,
            "name": "Default",
            "inviteCode": None,
            "inviteCodeCreatedMts": None,
            "ctaId": 8311,
            "organizationId": 1095,
            "description": "Volunteers who...",
        }
    ],
    "outreachEntries": [],
    "profileOrganizationTags": [
        {"profileEid": "ah9xl5wlv3i2t3", "tagId": 456196},
        {"profileEid": "akwimque10cov3", "tagId": 456196},
        {"profileEid": "aq0dx4hm8esd7u", "tagId": 456196},
    ],
}
