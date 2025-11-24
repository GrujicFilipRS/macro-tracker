<script setup lang="ts">

import { onMounted, ref } from 'vue';
import { GetUserPlans, type PlanInterface } from '../functions/GetUserPlans';
import { CheckIfEatenToday } from '../functions/CheckIfEatenToday';

import HeaderSection from './HeaderSection.vue';
import TodayOverview from './TodayOverview.vue';
import PlanSection from './PlanSection.vue';
import CreatePlanSection from './CreatePlanSection.vue';
import LogEaten from './LogEaten.vue';
import EatenToday from './EatenToday.vue';

const props = defineProps<{
    username: string;
}>();

const plans = ref<PlanInterface[]>([]);
const eatenToday = ref<boolean>(false);

onMounted(async () => {
    plans.value = await GetUserPlans();
    eatenToday.value = await CheckIfEatenToday();
});

</script>

<template>
    <main>
        <HeaderSection
            :username="props.username"
        />

        <TodayOverview
            :plans="plans"
        />
        
        <PlanSection
            v-if="plans.length > 0"
            :plans="plans"
        />

        <CreatePlanSection v-if="plans.length === 0"/>

        <EatenToday v-if="eatenToday" />

        <LogEaten />
    </main>
</template>

<style>
@import url('./MainPage.css');
</style>