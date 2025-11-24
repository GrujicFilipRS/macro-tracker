import { API_ROUTE } from "../api";

export interface PlanData {
    name: string;
    num_proteins: number;
    num_carbs: number;
    num_fats: number;
};

export const CreateNewPlan = async (planData: PlanData) => {
    const token = localStorage.getItem('jwt') || '';

    fetch(`${API_ROUTE}/plan/create_plan/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': token
        },
        body: JSON.stringify(planData)
    })
}