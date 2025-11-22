<script setup lang="ts">
import { ref } from 'vue';

const mode = ref<'signup' | 'login'>('signup');
</script>

<template>
    <div class="signup-overlay">
        <div class="signup-window">
            <div class="signup-top-section">
                <button
                    :class="['signup-mode-button', mode === 'signup' ? 'mode-active' : '']"
                    @click="mode = 'signup'"
                >
                    Sign Up
                </button>
                <button
                    :class="['signup-mode-button', mode === 'login' ? 'mode-active' : '']"
                    @click="mode = 'login'"
                >
                    Log In
                </button>
            </div>

            <div class="signup-form" v-show="mode === 'signup'">
                <form>
                    <label for="username">Username:</label>
                    <input
                        type="text"
                        name="username"
                        required
                    />

                    <label for="password">Password:</label>
                    <input
                        type="password"
                        name="password"
                        required
                    />

                    <label for="rptPassword">Repeat password:</label>
                    <input
                        type="password"
                        name="rptPassword"
                        required
                    />

                    <button type="submit">Sign up</button>
                </form>
            </div>

            <div class="login-form" v-show="mode === 'login'">
                <form>
                    <label for="username">Username:</label>
                    <input
                        type="text"
                        name="username"
                        required
                    />

                    <label for="password">Password:</label>
                    <input
                        type="password"
                        name="password"
                        required
                    />

                    <button type="submit">Log in</button>
                </form>
            </div>
        </div>
    </div>
</template>

<style>
@import url('./SignupWindow.css');
</style>