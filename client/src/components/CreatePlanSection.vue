<script setup lang="ts">
import { ref } from 'vue';
import PlanCreateWindow from './PlanCreateWindow.vue';

const showCreateWindow = ref<boolean>(false);

const OpenWindow = () => {
    showCreateWindow.value = true;
}

const CloseWindow = () => {
    showCreateWindow.value = false;
}

</script>

<template>
    <div class="page-section create-plan-section">
        <h2>You have no plans yet</h2>
        <p>Please create a plan to get started</p>
        <button @click="OpenWindow">Create Plan</button>
    </div>

    <PlanCreateWindow
        :close-window="CloseWindow"
        v-if="showCreateWindow"
    />
</template>

<style>
@import url('./CreatePlanSection.css');
</style>