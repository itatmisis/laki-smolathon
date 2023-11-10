<script>
    import Icon from "$lib/Icon.svelte";
</script>

<article>
    <header>
        <button>
            <Icon kind="back" />
        </button>
        <h1>Оставьте отзыв</h1>
    </header>
    <hr />
    <!-- TODO: Надпись "максимум 300 символов" -->
    <textarea placeholder="Скажите, что вы думаете об этом месте" />
    <label class="upload-image">
        <Icon kind="plus"/>
        Добавить фото
        <input
            type="file"
            style="display: none"
            name="image"
            accept="image/gif,image/jpeg,image/jpg,image/png"
            multiple
        />
    </label>
    <button>Отправить отзыв</button>
</article>

<style lang="scss">
    article {
        display: flex;
        flex-direction: column;
        background-color: var(--white1);
        border-radius: 8px;
        padding: 0 16px;

        header {
            display: flex;
            flex: 0 0 48px;
            align-items: center;
            button {
                --icon-size: 16px;
                padding: {
                    top: 16px;
                    bottom: 16px;
                    right: 12px;
                }
                border: 0;
                background-color: transparent;
                cursor: pointer;
            }
            h1 {
                font-size: 15px;
                height: 24px;
                line-height: 24px;
                font-weight: bold;
            }
        }
        hr {
            height: 1px;
            color: var(--white2);
            background-color: var(--white2);
            border-width: 0;
        }
        textarea {
            resize: none;
            margin: 16px 0;
            height: 90px;
            border: 0;
            color: var(--black);
            font-size: 15px;
            outline: none;
            &::placeholder {
                color: var(--gray-text);
            }
        }
        .upload-image {
            display: flex;
            gap: 8px;
            font-size: 15px;
            --icon-size: 12px;
            input[type="file"] {
                display: none;
            }
        }
        > button {
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: var(--emphis2);
            height: 40px;
            border: 0;
            border-radius: 8px;
            color: var(--white1);
            margin: {
                top: 24px;
                bottom: 12px;
            };
        }
    }
</style>
