<meta>
    <!-- 定義目標平台環境與引用的技能庫 (Path 2: Heterogeneous Strategy) -->
    <env target="WSL" />
    <tag name="c_standard_io" />
    <tag name="array_sort" />
</meta>

<constraint>
    static_memory
    no_malloc
    O(n^2)_acceptable
</constraint>

<evolution_ref>
    v3_base
</evolution_ref>

<body>
    @AI: Implement a main function sorting an array, ensuring memory constraints are met.
</body>
