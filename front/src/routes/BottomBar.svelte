<script lang="ts">
    import { goto } from "$app/navigation";
    import { page } from "$app/stores";
    import Icon from "$lib/Icon.svelte";

    type PageKind = (typeof pages)[number];

    const pages = [
        { path: "journal", name: "Дневник", icon: "journal" },
        { path: "map", name: "Карта", icon: "pointer" },
        { path: "profile", name: "Профиль", icon: "profile" }
    ] as const;

    let page_path: PageKind["path"] | undefined = undefined;

    $: if ($page.route.id == "/journal") {
        page_path = "journal";
    } else if ($page.route.id == "/profile") {
        page_path = "profile";
    } else if ($page.route.id == "/map") {
        page_path = "map";
    }

    const on_click = (_page: PageKind) => {
        goto(_page.path);
    };
</script>

<nav>
    {#each pages as _page}
        <button class:selected={_page.path == page_path} on:click={() => on_click(_page)}>
            <div class="icon-background">
                <Icon kind={_page.icon} />
            </div>
            <span>{_page.name}</span>
        </button>
    {/each}
</nav>

<style lang="scss">
    nav {
        display: flex;
        align-items: stretch;
        flex: 0 0 80px;

        button {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;

            flex: 1;
            border: 0;
            background-color: var(--button-color, var(--background-color, white));

            span {
                font-size: 13px;
            }

            > .icon-background {
                padding: 8px;

                width: 40px;
                height: 40px;
                --icon-size: 24px;
                border-radius: 8px;
            }

            &.selected {
                .icon-background {
                    --icon-invert: 1;
                    background-color: #262634;
                }
            }
        }
    }
</style>
