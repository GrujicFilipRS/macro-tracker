<script setup lang="ts">
import { ref } from 'vue';
import type { PlanInterface } from '../functions/GetUserPlans';

const props = defineProps<{
    plans: PlanInterface[];
}>();

const planSelected = ref<PlanInterface | undefined>(undefined);

const handlePlanSelect = (e: Event) => {
    const id = Number((e.target as HTMLInputElement).id);
    planSelected.value = props.plans.find(p => p.id === id) || undefined;
}

</script>

<template>
    <div class="plan-section">
        <div class="lside-plans">
            <div class="top-lside-plans">
                <h3>Your plans</h3>

                <button>+</button>
                <button :disabled="!planSelected">✎</button>
            </div>

            <p v-if="plans.length === 0">You currently have no plans</p>
            
            <div
                v-for="plan in props.plans"
                :key="plan.id"
            >
                <input
                    type="radio"
                    name="selectedPlan"
                    :id="plan.id.toString()"
                    :value="plan.name"
                    @change="handlePlanSelect"
                />
                <label :for="plan.id.toString()">
                {{ plan.name }}
                </label>
            </div>
        </div>
        
        <div v-if="planSelected" class="rside-plans">
            <p>Proteins: {{ planSelected.num_proteins }}</p>
            <p>Carbs: {{ planSelected.num_carbs }}</p>
            <p>Fats: {{ planSelected.num_fats }}</p>
        </div>

        <div v-if="!planSelected" class="rside-plans">
            <p>Please select a plan</p>
        </div>
    </div>
</template>

<style>
@import url('./PlanSection.css');
</style>