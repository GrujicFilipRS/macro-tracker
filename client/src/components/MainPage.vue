<script setup lang="ts">

import HeaderSection from './HeaderSection.vue';
import TodayOverview from './TodayOverview.vue';

const props = defineProps<{
    username: string;
}>();

</script>

<template>
    <main>
        <HeaderSection
            :username="props.username"
        />

        <TodayOverview />
    </main>
</template>

<style>
@import url('./MainPage.css');
</style>