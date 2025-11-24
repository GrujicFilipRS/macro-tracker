<script setup lang="ts">
import { ref } from 'vue';
import EatenCreateWindow from './EatenCreateWindow.vue';

const createWindowOpen = ref<boolean>(false);

</script>

<template>
    <div class="page-section log-food">
        <h2>Log Eaten Food</h2>
        <p>This is where you can log the food you have eaten.</p>
        <button @click="createWindowOpen = true">Log food</button>
    </div>

    <EatenCreateWindow
        v-if="createWindowOpen"
        :close-window="() => {createWindowOpen = false;}"
    />
</template>

<style>
@import url('./LogEaten.css');
</style>