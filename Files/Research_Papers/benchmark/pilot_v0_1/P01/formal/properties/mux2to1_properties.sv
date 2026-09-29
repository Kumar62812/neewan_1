// P01 shared formal contract.
// The same property module is instantiated by both validation harnesses.
module mux2to1_properties (
    input logic a,
    input logic b,
    input logic sel,
    input logic y
);

    // Immediate combinational assertion over the legal Boolean input domain.
    // No environmental assumptions are added.
    always @* begin
        assert (y == (sel ? b : a));
    end

endmodule
