module harness_reference;
    logic a, b, sel;
    logic y;

    mux2to1 dut (
        .a(a), .b(b), .sel(sel), .y(y)
    );

    mux2to1_properties props (
        .a(a), .b(b), .sel(sel), .y(y)
    );

    // No assumptions beyond the declared one-bit Boolean inputs.
endmodule
