import pytest
import requests
import os


ENDPOINT = "https://todo.pixegami.io"

response = requests.get(ENDPOINT,verify=False)
data = response.json()
statuscode = response.status_code
print(response)
print(data)
print(statuscode)

def test_can_call_endpoint():
    response = requests.get(ENDPOINT,verify=False)
    assert response.status_code == 200

def test_can_create_task():
    payload= payload_generator()
    create_task_response = create_task(payload)
    assert create_task_response.status_code==200
    create_task_data = create_task_response.json()

    task_id = get_task_id_from_data(create_task_data)
    get_task_response  = get_task(task_id)
    assert get_task_response.status_code==200
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]
    assert get_task_data["is_done"] == payload["is_done"]


def test_can_update_item():
    payload = payload_generator()
    task_response = create_task(payload)
    assert task_response.status_code == 200
    task_data = task_response.json()
    task_id = get_task_id_from_data(task_data)

    new_payload = {
        "content": "I am Neta",
        "user_id": "Oran",
        "task_id": task_id,
        "is_done": True
    }
    update_task_response = requests.put(ENDPOINT+"/update-task",json=new_payload,verify=False)
    assert update_task_response.status_code == 200
    get_task_response  = get_task(task_id)
    assert get_task_response.status_code==200
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == new_payload["content"]
    assert get_task_data["user_id"] == new_payload["user_id"]
    assert get_task_data["is_done"] == new_payload["is_done"]

def create_task(payload):
    return requests.put(ENDPOINT+"/create-task",json=payload,verify=False)

def get_task(task_id):
    return requests.get(ENDPOINT + f"/get-task/{task_id}", verify=False)

def list_task(user_id):
    return requests.get(ENDPOINT + f"/list-tasks/{user_id}", verify=False)

def delete_task(task_id):
    return requests.delete(ENDPOINT + f"/delete-task/{task_id}", verify=False)
def test_can_get_list_task():
    payload = payload_generator()
    new_task = create_task(payload)
    assert new_task.status_code == 200
    user_id = get_user_id_from_data(new_task.json())
    response_list_task = list_task(user_id)
    assert response_list_task.status_code == 200
    data = response_list_task.json()
    print(data)
    tasks = data["tasks"]

def test_can_delete_task():
    payload = payload_generator()
    new_task = create_task(payload)
    assert new_task.status_code == 200
    task_id = get_task_id_from_data(new_task.json())
    response_del_task = delete_task(task_id)
    assert response_del_task.status_code == 200

##todo fix this function
def test_can_delete_all_tasks():
    list_of_tasks = list_task("Oran")
    assert list_of_tasks.status_code == 200
    data = list_of_tasks.json()
    list_to_del = data["tasks"]
    print(list_to_del)
    for task in list_to_del:
        task_id = task["task_id"]
        delete_task(task_id)
    list_of_tasks = list_task("Oran")
    assert list_of_tasks.status_code == 200
    data = list_of_tasks.json()
    list_to_del = data["tasks"]
    print(list_to_del)
    assert len(list_to_del) == 0
def payload_generator():
    return {
        "content": "I am Oran",
        "user_id": "Oran",
        "is_done": False
    }
def get_task_id_from_data(data):
    return data["task"]["task_id"]

def get_user_id_from_data(data):
    return data["task"]["user_id"]

