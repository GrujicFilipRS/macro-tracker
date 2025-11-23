<script setup lang="ts">

import { onMounted, ref } from 'vue';
import { GetUserPlans, type PlanInterface } from '../functions/GetUserPlans';
import HeaderSection from './HeaderSection.vue';
import TodayOverview from './TodayOverview.vue';

const props = defineProps<{
    username: string;
}>();

const plans = ref<PlanInterface[]>();

onMounted(async () => {
    plans.value = await GetUserPlans();
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
    </main>
</template>

<style>
@import url('./MainPage.css');
</style>