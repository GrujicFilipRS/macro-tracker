import { API_ROUTE } from "../api";

export interface PlanInterface {
    id: number;
    name: string;
    num_proteins: number;
    num_carbs: number;
    num_fats: number;
}

export async function GetUserPlans(): Promise<PlanInterface[]> {
    const token = localStorage.getItem('jwt') || '';

    return await fetch(`${API_ROUTE}/plan/get_user_plans/`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': token
        }
    }).then(async res => {
        const data = await res.json();
        return data['plans'] as PlanInterface[];
    })
}