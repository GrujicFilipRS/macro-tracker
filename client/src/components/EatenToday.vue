<script lang="ts" setup>
import { onMounted, ref } from 'vue';
import type { FoodData } from '../functions/CreateFoodItem';
import { GetTodaysFood } from '../functions/GetTodaysFood';

const food = ref<FoodData[]>([]);

onMounted(async () => {
    food.value = await GetTodaysFood();
    console.log(food.value);
})

</script>

<template>
    <div class="page-section eaten-today">
        <h2>Eaten Today</h2>
        <div class="food-items">
            <p v-for="foodItem in food" :key="foodItem.id">{{ foodItem.food_item }}</p>
        </div>
    </div>
</template>

<style>
@import url('./EatenToday.css');
</style>