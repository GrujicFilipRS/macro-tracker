<script setup lang="ts">
import { reactive, ref } from 'vue';
import { HandleLogin, HandleSignup } from '../functions/HandleSignup';

const params = new URLSearchParams(window.location.search);

const signupError = params.get('signup_error');
const loginError = params.get('login_error');

const errors = new Map<string, string>([
    ['signup-pwd-no-match', 'Password and confirmation don\'t match'],
    ['signup-data-not-provided', 'Fill in all of the input fields!'],
    ['signup-invalid-data-format', 'Invalid input data format!'],
    ['signup-user-already-exists', 'User with such username already exists!'],
    
    ['login-invalid-data', 'Fill in all of the input fields!'],
    ['login-invalid-creds', 'Username or password incorrect!']
])

const mode = ref<'signup' | 'login'>('signup');

if (loginError !== null)
    mode.value = 'login'

const form = reactive({
    username: '',
    password: '',
    rptPassword: ''
});

const SignUp = async () => {
    if (form.password != form.rptPassword) {
        location.href = '/?signup_error=pwd-no-match';
        return;
    }

    const {status, message} = await HandleSignup(form.username, form.password);
    if (status === 201) {
        location.href = '/';
        return;
    }

    location.href=`/?signup_error=${message}`;
}

const LogIn = async () => {
    const {status, message} = await HandleLogin(form.username, form.password);
    if (status === 200) {
        location.href = '/';
        return;
    }

    location.href=`/?login_error=${message}`;
}

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
                <form @submit.prevent="SignUp">
                    <label for="username">Username:</label>
                    <input
                        type="text"
                        name="username"
                        v-model="form.username"
                        required
                    />

                    <label for="password">Password:</label>
                    <input
                        type="password"
                        name="password"
                        v-model="form.password"
                        required
                    />

                    <label for="rptPassword">Repeat password:</label>
                    <input
                        type="password"
                        name="rptPassword"
                        v-model="form.rptPassword"
                        required
                    />

                    <button type="submit">Sign up</button>

                    <p class="error-text" v-show="signupError !== null">
                        {{ errors.get(`signup-${signupError}`) || 'Unknown error' }}
                    </p>
                </form>
            </div>

            <div class="login-form" v-show="mode === 'login'">
                <form @submit.prevent="LogIn">
                    <label for="username">Username:</label>
                    <input
                        type="text"
                        name="username"
                        v-model="form.username"
                        required
                    />

                    <label for="password">Password:</label>
                    <input
                        type="password"
                        name="password"
                        v-model="form.password"
                        required
                    />

                    <button type="submit">Log In</button>

                    <p class="error-text" v-show="loginError !== null">
                        {{ errors.get(`login-${loginError}`) || 'Unknown error' }}
                    </p>
                </form>
            </div>
        </div>
    </div>
</template>

<style>
@import url('./SignupWindow.css');
</style>