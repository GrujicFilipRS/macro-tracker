<script setup lang="ts">
import { ref } from 'vue';

const mode = ref<'signup' | 'login'>('signup');
</script>

<template>
    <div class="signup-window">
        <div class="signup-top-section">
            <div
                :class="['signup-mode-button', mode === 'signup' ? 'mode-active' : '']"
                @click="mode = 'signup'"
            >
                Sign Up
            </div>
            <div
                :class="['signup-mode-button', mode === 'login' ? 'mode-active' : '']"
                @click="mode = 'login'"
            >
                Log In
            </div>
        </div>

        <div class="signup-form" v-show="mode === 'signup'">

        </div>

        <div class="login-form" v-show="mode === 'login'">

        </div>
    </div>
</template>

<style>
@import url('./SignupWindow.css');
</style>