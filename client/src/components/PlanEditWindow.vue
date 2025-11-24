<script setup lang="ts">
import { reactive, watch } from 'vue';
import type { PlanInterface } from '../functions/GetUserPlans';
import { EditPlan } from '../functions/EditWindow';


const props = defineProps<{
    plan: PlanInterface;
    closeWindow: any;
}>();

const planForm = reactive<PlanInterface>({
    id: 0,
    name: '',
    num_proteins: 0,
    num_carbs: 0,
    num_fats: 0,
});

const submitForm = () => {
    EditPlan(planForm).then(() => {
        props.closeWindow();
        location.reload();
    });
}

watch(() => props.plan,
    (plan) => {
        planForm.id = plan.id;
        planForm.name = plan.name;
        planForm.num_proteins = plan.num_proteins;
        planForm.num_fats = plan.num_fats;
        planForm.num_carbs = plan.num_carbs;
    },
{ immediate: true });

</script>

<template>
    <div class="plan-create-overlay">
        <div class="plan-create-window">
            <h2>Create New Plan</h2>
            <form @submit.prevent="submitForm">
                <div>
                    <label for="name">Plan Name: </label>
                    <input id="name" v-model="planForm.name" />
                </div>

                <div>
                    <label for="proteins">Proteins: </label>
                    <input type="number" id="proteins" v-model.number="planForm.num_proteins" />
                </div>

                <div>
                    <label for="carbs">Carbs: </label>
                    <input type="number" id="carbs" v-model.number="planForm.num_carbs" />
                </div>

                <div>
                    <label for="fats">Fats: </label>
                    <input type="number" id="fats" v-model.number="planForm.num_fats" />
                </div>

                <button type="submit">Submit</button>

            </form>
            <button @click="() => props.closeWindow()" class="cancel-btn">Cancel</button>
        </div>
    </div>
</template>

<style>
@import url('./PlanCreateWindow.css');
</style>