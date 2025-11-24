import { API_ROUTE } from "../api";
import type { PlanInterface } from "./GetUserPlans";

export const EditPlan = async (plan: PlanInterface) => {
    return fetch(`${API_ROUTE}/plan/update_plan/?plan_id=${plan.id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': localStorage.getItem('jwt') || ''
        },
        body: JSON.stringify(plan)
    })
}