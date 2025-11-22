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
        if (!res.ok) {
            return (res.status, data['message']);
        }

        return data['token'];
    })
}

export const HandleLogin = async () => {

}