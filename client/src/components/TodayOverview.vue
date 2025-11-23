<script setup lang="ts">

import { onMounted, ref } from 'vue';

import Slider from './Slider.vue';

import { GetTodaysMacros } from '../functions/GetTodaysMacros';
import type { MacrosInterface } from '../functions/MacrosInterface';
import type { PlanInterface } from '../functions/GetUserPlans';

const macros = ref<MacrosInterface>({} as MacrosInterface);
const defaultPlan: MacrosInterface = {
    proteins: 150,
    carbs: 200,
    fats: 70
};

const props = defineProps<{
    plans: PlanInterface[] | undefined;
}>();

const selectedPlan = ref<PlanInterface | undefined>(undefined);
onMounted(async () => {
    macros.value = await GetTodaysMacros();
    selectedPlan.value = props.plans && props.plans.length > 0 ? props.plans[0] : undefined;
});

const handlePlanSelect = (e: Event) => {
    const id = Number((e.target as HTMLSelectElement).value);
    selectedPlan.value = props.plans!.find(p => p.id === id) || undefined;
}

</script>

<template>
    <div class="today-overview">
        <div class="lside-today">
            <h3 style="font-size: 20px">TODAY</h3>
            <label for="today-plans">Selected plan:</label>
            <select
                id="today-plans"
                name="today-plans"
                @change="handlePlanSelect"
            >
                <option
                    value=""
                    disabled
                    selected
                    v-if="!props.plans || props.plans.length === 0"
                >
                    Create a plan
                </option>

                <option
                    v-for="plan in props.plans"
                    :key="plan.id"
                    :value="plan.id"
                >
                    {{ plan.name }}
                </option>
            </select>
        </div>

        <div class="rside-today">
            <Slider
                name="Proteins"
                :currentValue="macros.proteins"
                :maxValue="selectedPlan ? selectedPlan.num_proteins : defaultPlan.proteins"
                fillColor="#9a38ba"
            />

            <Slider
                name="Carbs"
                :currentValue="macros.carbs"
                :maxValue="selectedPlan ? selectedPlan.num_carbs : defaultPlan.carbs"
                fillColor="#5938ba"
            />

            <Slider
                name="Fats"
                :currentValue="macros.fats"
                :maxValue="selectedPlan ? selectedPlan.num_fats : defaultPlan.fats"
                fillColor="#2727c4"
            />
        </div>
    </div>
</template>

<style>
@import url('./TodayOverview.css');
</style>