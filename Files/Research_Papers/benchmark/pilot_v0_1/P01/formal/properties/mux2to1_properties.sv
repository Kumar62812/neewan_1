// P01 shared formal contract.
// The same property module is instantiated by both validation harnesses.
module mux2to1_properties (
    input logic a,
    input logic b,
    input logic sel,
    input logic y
);

    // For Boolean inputs, the output must equal the selected input.
    always_comb begin
        assert (y == (sel ? b : a));
    end

endmodule
