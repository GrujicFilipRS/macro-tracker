import { API_ROUTE } from "../api";

export const DeletePlan = async (planId: number) => {
    const token = localStorage.getItem('jwt') || '';

    return fetch(`${API_ROUTE}/plan/delete_plan/?plan_id=${planId}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': token
        }
    })
}