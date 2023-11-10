<script lang="ts">
    import Icon from "$lib/Icon.svelte";

    export let name: string;
</script>

<section>
    <!-- svelte-ignore a11y-missing-attribute -->
    <img class="profile-picture" src="https://www.techcult.ru/content/2021/9865/chelovek-drakon.jpg"/>
    <div>
        <h1>{name}</h1>
        <!-- TODO: time from registration -->
        <h2>На ресурсе с {"placeholder"}</h2>
    </div>
    <button><Icon kind="edit"/></button>
</section>

<style lang="scss">
    section {
        display: flex;
        align-items: center;
        gap: 20px;
        img {
            aspect-ratio: 1;
            width: 80px;
            height: 80px;
            border-radius: 80px;
            overflow: hidden;
            object-fit: cover;
        }
        div {
            flex: 1;
            display: flex;
            flex-direction: column;
            h1 {
                font-size: 15px;
                font-weight: bold;
            }
            h2 {
                font-size: 13px;
                color: #727272;
            }
        }
        button {
            --icon-size: 20px;
            padding: 8px;
            border-radius: 8px;
            border: 0;
        }
    }
</style>