<meta>
    <env target="WSL" />
    <tag name="c_standard_io" />
    <tag name="array_sort" />
</meta>

<injection source="config/app.json" />

<constraint>
    static_memory
    no_malloc
    max_temp: 100
</constraint>

<evolution_ref>
    v4_base
</evolution_ref>

<body>
    @AI: Implement a daemon looping function that prints the $TEMP setting. Ensure Clean Shutdown Protocol on SIGTERM.
</body>
