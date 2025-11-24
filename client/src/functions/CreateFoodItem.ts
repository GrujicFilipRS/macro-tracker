import { API_ROUTE } from "../api";

export interface FoodData {
    id: number;
    food_item: string;
    datetime_eaten: string;
    num_proteins: number;
    num_carbs: number;
    num_fats: number;
    user_id: number;
}

export const LogNewFood = async (foodItem: FoodData) => {
    const token = localStorage.getItem('jwt') || '';

    return fetch(`${API_ROUTE}/eaten/create_eaten/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': token
        },
        body: JSON.stringify(foodItem)
    });
}