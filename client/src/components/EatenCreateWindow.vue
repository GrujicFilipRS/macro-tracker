<script setup lang="ts">

import { reactive } from 'vue';
import { LogNewFood, type FoodData } from '../functions/CreateFoodItem';

const props = defineProps<{closeWindow: any}>();

const planForm = reactive<FoodData>({
    id: 0,
    food_name: '',
    num_proteins: 0,
    num_carbs: 0,
    num_fats: 0,
    datetime_eaten: ''
});

const submitForm = () => {
    LogNewFood(planForm).then(() => {
        props.closeWindow();
        // location.reload();
    });
}

</script>

<template>
    <div class="plan-create-overlay">
        <div class="plan-create-window">
            <h2>Log new food item</h2>
            <form @submit.prevent="submitForm">
                <div>
                    <label for="name">Plan Name: </label>
                    <input id="name" v-model="planForm.food_name" />
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