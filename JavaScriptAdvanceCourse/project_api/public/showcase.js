Vue.component('showcase',
    {
        template: `
        <div class="goods-list">
            <card v-for="item of list" :good="item" :actionname="'Buy'"></card>
        </div>
        `,
        props: ['list']
    }
)