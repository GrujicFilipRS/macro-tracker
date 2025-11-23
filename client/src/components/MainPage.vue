<script setup lang="ts">

import HeaderSection from './HeaderSection.vue';
import TodayOverview from './TodayOverview.vue';

const props = defineProps<{
    username: string;
}>();

</script>

<template>
    <HeaderSection
        :username="props.username"
    />

    <TodayOverview />
</template>

<style>
@import url('./MainPage.css');
</style>