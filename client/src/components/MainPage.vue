<script setup lang="ts">

import { onMounted, ref } from 'vue';
import { GetUserPlans, type PlanInterface } from '../functions/GetUserPlans';
import HeaderSection from './HeaderSection.vue';
import TodayOverview from './TodayOverview.vue';
import PlanSection from './PlanSection.vue';
import CreatePlanSection from './CreatePlanSection.vue';
import LogEaten from './LogEaten.vue';
import EatenToday from './EatenToday.vue';
import { CheckIfEatenToday } from '../functions/CheckIfEatenToday';

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

        <EatenToday v-if="eatenToday" />

        <CreatePlanSection v-if="plans.length === 0"/>

        <LogEaten />
    </main>
</template>

<style>
@import url('./MainPage.css');
</style>