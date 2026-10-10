ticket1 = {
    "id": "TKT-101",
    "title": "Wi-Fi connection failure",
    "category": "Network",
    "urgency": "high",
    "affected_users": 15,
    "priority": "high",
    "status": "open",
    "assigned_to": "Grace"
    }

ticket2 = {
    "id": "TKT-102",
    "title": "Classroom projector failure",
    "category": "Equipment",
    "urgency": "medium",
    "affected_users": 30,
    "priority": "medium",
    "status": "open",
    "assigned_to": None
    }

tickets = [ticket1, ticket2]
print(ticket2["title"])
print(ticket1["assigned_to"])
