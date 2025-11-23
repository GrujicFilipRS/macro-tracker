<script setup lang="ts">
import { onMounted, ref } from 'vue';

import SignupWindow from './components/SignupWindow.vue';
import MainPage from './components/MainPage.vue';
import { VerifyJWT } from './api';

const showSignupWindow = ref<boolean>(false);
const username = ref<string>('');

onMounted(async () => {
    const token = localStorage.getItem('jwt') || '';
    const verification = await VerifyJWT(token);

    if (verification.statusCode !== 200) {
        showSignupWindow.value = true;
    }

    username.value = verification.data.username || '';
});

</script>

<template>
    <SignupWindow v-if="showSignupWindow" />
    <MainPage
        v-if="!showSignupWindow"
        :username="username"
    />
</template>

<style scoped>

</style>