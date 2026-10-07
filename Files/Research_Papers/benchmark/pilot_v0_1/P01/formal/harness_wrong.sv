module harness_wrong;
    logic a, b, sel;
    logic y;

    mux2to1 dut (
        .a(a), .b(b), .sel(sel), .y(y)
    );

    // Exactly the same property module and contract as the reference run.
    mux2to1_properties props (
        .a(a), .b(b), .sel(sel), .y(y)
    );

    // No assumptions beyond the declared one-bit Boolean inputs.
endmodule
