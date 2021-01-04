const snackList = props => (
    <>
        <h2>Snacks</h2>
        <ul>
            {props.snacks.map((snack) => (
                <li key={snack.id}>
                    <section>
                        <h3>{snack.name}</h3>
                        <p>{snack.description}</p>
                    </section>
                </li>
            ))}
        </ul>
    </>
)

export default snackList;
