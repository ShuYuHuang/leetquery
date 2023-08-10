"""
Copyright (c) 2023 Shu-Yu Huang

Licensed under the MIT License
"""
import json
from typing import List
import requests

__all__  = ["get_submissions"]

def get_submissions(username: str="syhaung", limit: int=12, title_only: bool=True) -> List[str]:
    """
        Gwt
    """
    url = "https://leetcode.com/graphql?"
    headers = {'Content-Type': 'application/json'}
    query = """
    query recentAcSubmissions($username: String!, $limit: Int!) {
        recentAcSubmissionList(username: $username, limit: $limit) {
            id
            title
            titleSlug
            timestamp
        }
    }
    """
    variables = {'username': username, 'limit': limit}
    payload = {
            'query': query,
            'operationName': 'recentAcSubmissions',
            'variables': variables
    }

    response = requests.post(
        url,
        headers=headers,
        data=json.dumps(payload),
        timeout=1.5
    ).json()

    if title_only:
        return [x["title"] for x in response["data"]["recentAcSubmissionList"]]
    else:
        return [x for x in response["data"]["recentAcSubmissionList"]]
