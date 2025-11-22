<script setup lang="ts">
import { onMounted, ref } from 'vue';

import SignupWindow from './components/SignupWindow.vue';
import { VerifyJWT } from './api';

const showSignupWindow = ref<boolean>(false);

onMounted(async () => {
    const token = localStorage.getItem('jwt') || '';
    const verification = await VerifyJWT(token);

    if (verification.statusCode !== 200) {
        showSignupWindow.value = true;
    }
});

</script>

<template>
    <SignupWindow v-show="showSignupWindow" />
</template>

<style scoped>

</style>