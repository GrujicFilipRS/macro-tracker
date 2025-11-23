<script setup lang="ts">

const props = defineProps<{
    name: string;
    currentValue: number;
    maxValue: number;
    fillColor?: string;
}>();

</script>

<template>
    <div class="slider-container">
        <label for="slider">{{ props.name }}:</label>
        <div class="rside-slider">
            <input
                type="range"
                id="slider"
                :max="maxValue"
                :value="currentValue"
                :style="{
                    '--slider-fill': props.fillColor || '#4caf50'
                }"
                disabled
            />
            <p>{{ props.currentValue }}g / {{ props.maxValue }}g</p>
        </div>
    </div>
</template>

<style>
@import url('./Slider.css');
</style>