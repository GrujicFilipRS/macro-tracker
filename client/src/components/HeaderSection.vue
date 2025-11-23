<script setup lang="ts">

const props = defineProps<{
    username: string;
}>();

const HandleLogout = () => {
    localStorage.removeItem('jwt');
    window.location.reload();
};

</script>

<template>
    <header>
        <h2>Welcome, {{ props.username }}</h2>
        <img
            src="/logout.png"
            alt="Log out"
            @click="() => HandleLogout()"
        />
    </header>
</template>

<style>
@import url('./HeaderSection.css');
</style>