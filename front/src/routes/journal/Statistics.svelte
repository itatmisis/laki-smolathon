<div>
    <p class="overall">
        Вы посетили <mark>88</mark> Смоленских место<br />
        Заполнили дневник для <mark>12</mark> из них<br />
    </p>
    <div class="categories">
        <span>
            <mark>5</mark>
            Соборов
        </span>
        <span>
            <mark>5</mark>
            Музеев
        </span>
        <span>
            <mark>5</mark>
            Памятников
        </span>
    </div>
</div>

<style lang="scss">
    .overall {
        font-size: 15px;
        > mark {
            background-color: #d9d9d9;
            padding: 2px 8px;
            border-radius: 8px;
        }
        margin-bottom: 8px;
    }
    .categories {
        display: flex;
        gap: 4px;
        > span {
            display: flex;
            align-items: center;
            gap: 4px;
            background-color: #727272;
            color: white;
            padding: 8px;
            border-radius: 8px;
            font-size: 13px;

            > mark {
                display: flex;
                align-items: center;
                justify-content: center;
                width: 16px;
                height: 16px;
                text-align: center;
                color: #727272;
                background-color: #d9d9d9;
                border-radius: 2px;
            }
        }
    }
</style>
