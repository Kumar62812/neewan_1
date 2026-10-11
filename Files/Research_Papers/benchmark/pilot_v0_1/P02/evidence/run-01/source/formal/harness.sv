module harness;
    (* anyseq *) reg clk, rst, d;
    wire q;
`ifdef WRONG
    p02_wrong dut(clk, rst, d, q);
`else
    p02_register dut(clk, rst, d, q);
`endif
    p02_properties properties(clk, rst, d, q);
    reg past_valid = 1'b0;
    always @($global_clock) begin
        past_valid <= 1;
        if (!past_valid) assume(!clk);
        // Define setup at a sampled edge; inputs may change at every non-rising step.
        if (past_valid && !$past(clk) && clk) begin
            assume(rst == $past(rst));
            assume(d == $past(d));
        end
    end
endmodule
