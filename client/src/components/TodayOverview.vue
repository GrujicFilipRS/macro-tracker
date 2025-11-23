<script setup lang="ts">

import { onMounted, ref } from 'vue';

import Slider from './Slider.vue';

import { GetTodaysMacros } from '../functions/GetTodaysMacros';

const macros = ref<{
    proteins: number;
    carbs: number;
    fats: number;
}>({
    proteins: 0,
    carbs: 0,
    fats: 0,
});

onMounted(async () => {
    macros.value = await GetTodaysMacros();
});

</script>

<template>
    <div class="today-overview">
        <div class="lside-today">
            <h3>TODAY</h3>
            <label for="today-plans">Selected plan:</label>
            <select id="today-plans" name="today-plans">
                <option value="plan1">Plan 1</option>
                <option value="plan2">Plan 2</option>
                <option value="plan3">Plan 3</option>
            </select>
        </div>

        <div class="rside-today">
            <Slider
                name="Proteins"
                :currentValue="macros.proteins"
                :maxValue="150"
                fillColor="#9a38ba"
            />

            <Slider
                name="Carbs"
                :currentValue="macros.carbs"
                :maxValue="150"
                fillColor="#5938ba"
            />

            <Slider
                name="Fats"
                :currentValue="macros.fats"
                :maxValue="150"
                fillColor="#2727c4"
            />
        </div>
    </div>
</template>