<script setup lang="ts">

import HeaderSection from './HeaderSection.vue';

const props = defineProps<{
    username: string;
}>();

</script>

<template>
    <HeaderSection
        :username="props.username"
    />
</template>

<style>
@import url('./MainPage.css');
</style>