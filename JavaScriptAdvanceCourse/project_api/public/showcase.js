Vue.component('showcase',
    {
        template: `
        <div class="goods-list">
            <card v-for="item of list" :good="item" \
            v-on:add="addGood($event)"></card>
        </div>
        `,
        props: ['list'],
        methods: {
            async postData(url = '', data = {}) {
                const response = await fetch(url, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                });
                return await response;
            },

            addGood(id) {
                this.$emit('update:cart:add', id)
            }
        }
    }
)