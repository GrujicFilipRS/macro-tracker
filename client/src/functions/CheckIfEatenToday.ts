import { API_ROUTE } from "../api";

export const CheckIfEatenToday = async () => {
    const token = localStorage.getItem('jwt') || '';
    return fetch(`${API_ROUTE}/eaten/user_ate_today/`, {
        method: 'GET',
        headers: {
            'Authorization': `${token}`,
            'Content-Type': 'application/json',
        },
    }).then(response => response.json()).then(data => {
        return data.ate_today as boolean;
    })
}