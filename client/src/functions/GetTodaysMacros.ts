import { API_ROUTE } from '../api'

interface EatenData {
    id: number;
    user_id: number;
    food_item: string;
    datetime_eaten: string;
    num_proteins: number;
    num_carbs: number;
    num_fats: number;
}

export const GetTodaysMacros = async () => {
    const token = localStorage.getItem('jwt') || '';

    return fetch(`${API_ROUTE}/eaten/get_today_eaten/`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': token
        }
    }).then(async res => {
        const data = await res.json();

        const eatenData = data['eaten'] as EatenData[];

        let totalProteins = 0;
        let totalCarbs = 0;
        let totalFats = 0;

        eatenData.forEach(item => {
            totalProteins += item.num_proteins;
            totalCarbs += item.num_carbs;
            totalFats += item.num_fats;
        });

        return {
            proteins: totalProteins,
            carbs: totalCarbs,
            fats: totalFats
        };
    })
}