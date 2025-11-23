import { API_ROUTE } from '../api'

import type { MacrosInterface } from './MacrosInterface';

interface EatenData {
    id: number;
    user_id: number;
    food_item: string;
    datetime_eaten: string;
    num_proteins: number;
    num_carbs: number;
    num_fats: number;
}

export async function GetTodaysMacros(): Promise<MacrosInterface> {
    const token = localStorage.getItem('jwt') || '';

    return await fetch(`${API_ROUTE}/eaten/get_today_eaten/`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': token
        }
    }).then(async res => {
        const data = await res.json();

        const eatenData = data['eaten'] as EatenData[];

        let macros = {
            proteins: 0,
            carbs: 0,
            fats: 0
        } as MacrosInterface;

        eatenData.forEach(item => {
            macros.proteins += item.num_proteins;
            macros.carbs += item.num_carbs;
            macros.fats += item.num_fats;
        });

        return macros;
    })
}