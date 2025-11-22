import { API_ROUTE } from "../api"

export const HandleSignup = async (username: string, password: string) => {
    return fetch(`${API_ROUTE}/user/register/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username: username,
            password: password
        })
    }).then(async res => {
        const data = await res.json();
        if (res.status === 201)
            localStorage.setItem('jwt', data['token']);

        return {status: res.status, message: data['message']};
    })
}

export const HandleLogin = async (username: string, password: string) => {
    return fetch(`${API_ROUTE}/user/login/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username: username,
            password: password
        })
    }).then(async res => {
        const data = await res.json();
        if (res.ok)
            localStorage.setItem('jwt', data['token']);

        return {status: res.status, message: data['message']};
    })
}