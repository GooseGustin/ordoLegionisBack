NIL = 'NIL'
NON = '-'
NULL = ""

###########################################
curia = {
    "id": 2,
    "name": "Our Lady Virgin Most Prudent",
    "iden": "V347POM20L",
    "inaug_date": "2000-01-02",
    "email": "virginmostprudent2018@gmail.com",
    "state": "Plateau",
    "country": "Nigeria",
    "archdiocese": "Jos",
    "parish": "St. Finbarr's Catholic Church, Rayfield, Jos",
    "creator": 1,
    "created_at": "2025-03-19T08:28:49.788348Z",
    "managers": [
        1
    ],
    "management_requests": []
}
# -------------------------------------
praesidium = {
    "id": 2,
    "name": "Our Lady Mother of Good Counsel",
    "state": "Plateau",
    "country": "Nigeria",
    "parish": "St. Peter's Catholic Church, Topp",
    "curia": 2,
    "iden": "CoLMG27301O",
    "address": "Inside the church",
    "meeting_time": "Every Sunday at 7:30 AM",
    "inaug_date": "2022-02-05",
    "spiritual_director": "Fr. Peter Zakka Daluk",
    "spiritual_director_app_date": "2025-02-07",
    "president": "Bro. Mafeng Pam",
    "pres_app_date": "2024-03-10",
    "vice_president": "Sis. Josephine Dung",
    "vp_app_date": "2023-09-10",
    "secretary": "Sis. Kangyang Pam",
    "sec_app_date": "2022-02-05",
    "treasurer": "Sis. Peace Yakubu",
    "tres_app_date": "2022-02-05",
    "managers": [
        1
    ],
    "members": [
        1
    ],
    "membership_requests": [],
    "next_report_deadline": "2025-04-13",
    "created_at": "2025-03-19T08:39:36.041958Z",
    "reports": [
        17
    ]
}
# -----------------------------------------------
report = {
    "id": 20,
    "praesidium": 2,
    "submission_date": "2025-03-30",
    "last_submission_date": "2024-04-21",
    "report_number": 4,
    "report_period": 0,
    "last_curia_visit_date": "2025-03-23",
    "last_curia_visitors": "Sis. Victoria Pam from Ark of the Covenant, Mazaram",
    "officers_curia_attendance": {
        "President": 0,
        "Vice President": 0,
        "Secretary": 0,
        "Treasurer": 0
    },
    "no_curia_meetings_held": {
        "President": 12,
        "Vice President": 12,
        "Secretary": 12,
        "Treasurer": 12
    },
    "no_praesidium_meetings_held": {
        "President": 48,
        "Vice President": 48,
        "Secretary": 48,
        "Treasurer": 48
    },
    "no_curia_meetings_held_previous": {
        "President": 13,
        "Vice President": 13,
        "Secretary": 13,
        "Treasurer": 13
    },
    "no_praesidium_meetings_held_previous": {
        "President": 49,
        "Vice President": 49,
        "Secretary": 49,
        "Treasurer": 49
    },
    "officers_meeting_attendance": {
        "President": 44,
        "Vice President": 48,
        "Secretary": 28,
        "Treasurer": 38
    },
    "extension_plans": "Recruit more members",
    "auditor1": "Bro. James Kim Yop", 
    "auditor2": 'Sis. Amelia Rose',
    "problems": "",
    "remarks": "",
    "no_meetings_expected": 49,
    "no_meetings_held": 48,
    "avg_attendance": 6,
    "poor_attendance_reason": "Most members are students",
    "membership_details": 24,
    "include_intermediate": True,
    "achievements": {
        "id": 44,
        "no_recruited": [
            1,
            0
        ],
        "no_baptized": [
            0,
            0
        ],
        "no_confirmed": [
            0,
            0
        ],
        "no_first_communicants": [
            0,
            0
        ],
        "no_married": [
            0,
            0
        ],
        "no_vocations": [
            0,
            0
        ],
        "no_converted": [
            0,
            0
        ],
        "others": {}
    },
    "function_attendances": [
        257,
        258,
        259,
        260,
        261,
        262,
        263,
        264,
        265,
        266,
        267,
        268,
        269,
        270
    ],
    "work_total_and_average": {
        "Home Visitation": {
            "total": True,
            "average": False
        },
        "Crowd Contact": {
            "total": True
        },
        "Catechism Instruction": {
            "total": True,
            "average": True
        },
        "Care for Children at Mass": {
            "total": True,
            "average": True
        },
        "Care for the Junior Praesidium": {
            "total": True,
            "average": True
        }
    },
    "patricians_start": "2024-04",
    "patricians_end": "2025-03",
    "work_summaries": [
        137,
        138,
        139,
        140,
        141,
        142
    ],
    "financial_summary": {
        "id": 20,
        "report": 20,
        "month_year": [
            [
                "Apr",
                2024
            ],
            [
                "May",
                2024
            ],
            [
                "Jun",
                2024
            ],
            [
                "Jul",
                2024
            ],
            [
                "Aug",
                2024
            ],
            [
                "Sep",
                2024
            ],
            [
                "Oct",
                2024
            ],
            [
                "Nov",
                2024
            ],
            [
                "Dec",
                2024
            ],
            [
                "Jan",
                2025
            ],
            [
                "Feb",
                2025
            ],
            [
                "Mar",
                2025
            ]
        ],
        "acf": [
            0,
            90,
            330,
            520,
            650,
            1050,
            680,
            2030,
            520,
            1610,
            2590,
            220
        ],
        "sbc": [
            490,
            940,
            1140,
            1030,
            900,
            1480,
            1350,
            690,
            1090,
            1380,
            930,
            770
        ],
        "balance": [
            90,
            330,
            520,
            650,
            1550,
            680,
            2030,
            520,
            1610,
            2590,
            220,
            790
        ],
        "expenses": {
            "bouquet": [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
            ],
            "stationery": [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0
            ],
            "altar": [
                0,
                0,
                0,
                0,
                0,
                100,
                0,
                0,
                0,
                0,
                0,
                0
            ],
            "extension": [
                400,
                200,
                450,
                400,
                500,
                550,
                0,
                0,
                0,
                400,
                0,
                0
            ],
            "remittance": [
                0,
                0,
                500,
                500,
                0,
                0,
                0,
                1200,
                0,
                0,
                3300,
                200
            ],
            "others": [
                [],
                [
                    {
                        "Booking of Edel Quinn Mass": 500
                    }
                ],
                [],
                [],
                [],
                [
                    {
                        "Booking of Mary's birthday Mass": 500
                    },
                    {
                        "Mary's birthday transportation of juniors": 700
                    }
                ],
                [],
                [
                    {
                        "Booking of departed legionaries Mass": 500
                    },
                    {
                        "Booking of Frank Duff's Mass": 500
                    }
                ],
                [],
                [],
                [],
                []
            ]
        },
        "report_production": 0,
        "balance_at_hand": 0
    },
    "audited": False,
    "previous_curia_attendance": {
        "President": 0,
        "Vice President": 0,
        "Secretary": 0,
        "Treasurer": 0
    },
    "previous_meeting_attendance": {
        "President": 0,
        "Vice President": 0,
        "Secretary": 0,
        "Treasurer": 0
    },
    "read_and_accepted": True,
    "conclusion": "This report was carefully extracted from the records of the praesidium, which include the worksheet, roll call book, minutes book, and treasurer's book.",
    "membership": {
        "id": 24,
        "affiliated_praesidia": [
            0,
            0,
            0
        ],
        "active_members": [
            0,
            0,
            0
        ],
        "probationary_members": [
            0,
            0,
            0
        ],
        "auxiliary_members": [
            0,
            0,
            0
        ],
        "adjutorian_members": [
            0,
            0,
            0
        ],
        "praetorian_members": [
            0,
            0,
            0
        ]
    },
    "fxn_attendances": [
        {
            "id": 257,
            "name": "Acies",
            "date": None,
            "current_year_attendance": 0,
            "previous_year_attendance": 0,
            "report": 20
        },
        {
            "id": 258,
            "name": "May Devotion",
            "date": "2024-05-01",
            "current_year_attendance": 0,
            "previous_year_attendance": 0,
            "report": 20
        },
        {
            "id": 259,
            "name": "Edel Quinn Mass",
            "date": "2024-05-12",
            "current_year_attendance": 0,
            "previous_year_attendance": 0,
            "report": 20
        },
        {
            "id": 260,
            "name": "Annual Enclosed Retreat",
            "date": None,
            "current_year_attendance": 0,
            "previous_year_attendance": 0,
            "report": 20
        },
        {
            "id": 261,
            "name": "Mary's Birthday",
            "date": "2024-09-08",
            "current_year_attendance": 0,
            "previous_year_attendance": 0,
            "report": 20
        },
        {
            "id": 262,
            "name": "Officers' Workshop",
            "date": None,
            "current_year_attendance": 0,
            "previous_year_attendance": 0,
            "report": 20
        },
        {
            "id": 263,
            "name": "October Devotion",
            "date": "2024-10-01",
            "current_year_attendance": 0,
            "previous_year_attendance": 0,
            "report": 20
        },
        {
            "id": 264,
            "name": "Departed Legionaries' Mass",
            "date": "2024-11-02",
            "current_year_attendance": 0,
            "previous_year_attendance": 0,
            "report": 20
        },
        {
            "id": 265,
            "name": "Frank Duff's Mass",
            "date": "2024-11-12",
            "current_year_attendance": 0,
            "previous_year_attendance": 0,
            "report": 20
        },
        {
            "id": 266,
            "name": "Legion Congress",
            "date": None,
            "current_year_attendance": 0,
            "previous_year_attendance": 0,
            "report": 20
        },
        {
            "id": 267,
            "name": "Patrician Meetings",
            "date": None,
            "current_year_attendance": 3,
            "previous_year_attendance": 4,
            "report": 20
        },
        {
            "id": 268,
            "name": "Annual General Reunion",
            "date": None,
            "current_year_attendance": 0,
            "previous_year_attendance": 0,
            "report": 20
        },
        {
            "id": 269,
            "name": "Exporatio Dominicalis",
            "date": None,
            "current_year_attendance": 0,
            "previous_year_attendance": 0,
            "report": 20
        },
        {
            "id": 270,
            "name": "Outdoor Function",
            "date": None,
            "current_year_attendance": 0,
            "previous_year_attendance": 0,
            "report": 20
        }
    ],
    "work_summary": [
        {
            "type": "Home Visitation",
            "active": True,
            "no_done": 32,
            "no_assigned": 46,
            "details": {
                "No. of active Catholics": 121,
                "No. of inactive Catholics": 145,
                "No. of separated brethren": 157,
                "No. of homes": 131,
                "No. of unknowns": 2
            }
        },
        {
            "type": "Crowd Contact",
            "active": True,
            "no_done": 16,
            "no_assigned": 32,
            "details": {
                "No. of inactive Catholics": 9,
                "No. of separated brethren": 18,
                "No. of muslims": 2,
                "No. of active Catholics": 31
            }
        },
        {
            "type": "Catechism Instruction",
            "active": True,
            "no_done": 30,
            "no_assigned": 38,
            "details": {
                "No. of catechumen": 416
            }
        },
        {
            "type": "Care for Children at Mass",
            "active": True,
            "no_done": 47,
            "no_assigned": 47,
            "details": {
                "No. of children": 2946
            }
        },
        {
            "type": "Care for the Junior Praesidium",
            "active": True,
            "no_done": 49,
            "no_assigned": 49,
            "details": {
                "No. of children": 843
            }
        },
        {
            "type": "Praying the rosary",
            "active": False,
            "no_done": 2,
            "no_assigned": 11,
            "details": {}
        }
    ]
}