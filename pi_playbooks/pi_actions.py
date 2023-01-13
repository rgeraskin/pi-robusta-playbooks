from robusta.api import MarkdownBlock, PrometheusKubernetesAlert, action


@action
def tag_tg_user(alert: PrometheusKubernetesAlert):
    users = {
        # back
        "alexander.apostolov": "Aps",
        "p.kuzmin": "@pabel0071",
        # front
        "mrs4z1337": "@mrs4z",
        "zhitenev.andr": "@kraavc",
        # other
        "rodionkislov": "@rodionkislov",
        "rgeraskin": "@rgeraskin"
    }

    labels = alert.alert.labels
    if "userUsername" in labels and labels['userUsername'] != "<no value>":
        if labels["userUsername"] in users:
            user_info = f"Commit author: {users[labels['userUsername']]}"
            alert.add_enrichment([MarkdownBlock(user_info)])
        else:
            user_info = "_No user info in action_ "
            alert.add_enrichment([MarkdownBlock(user_info)])
    # else:
    #     user_info = "_No user info in alert_"
