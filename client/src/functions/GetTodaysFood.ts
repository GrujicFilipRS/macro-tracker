import { API_ROUTE } from "../api"
import type { FoodData } from "./CreateFoodItem";

export const GetTodaysFood = async () => {
    const token = localStorage.getItem('jwt') || '';

    return fetch(`${API_ROUTE}/eaten/get_today_eaten/`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': token
        }
    }).then(async res => {
        const data = await res.json();
        return data['eaten'] as FoodData[];
    })
}