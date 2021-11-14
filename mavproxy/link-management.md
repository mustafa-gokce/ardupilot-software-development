# Link Management in MAVProxy
1. Start using: `mavproxy.py`
2. Show link statistics: `link`
3. Display link help screen: `link help`
4. List existing links: `link list`
5. Add a link to autopilot: `link add X:Y` where `X` is connection string and `Y` is an optional label.
   1. `X` is the connection string and covered before in [here](mavproxy-quickstart.md).
   2. `Y` is the label to make the link memorable, example label: `{"label":"your_link_name"}`
   3. Before adding a serial link run the command `set baudrate X` where `X` in the baud rate value.
6. Remove a link using: `link remove X` where `X` can be the link index or label.
7. Start high latency mode: `link hl on`
8. Stop high latency mode: `link hl off`
9. Reset statistics: `link resetstats`
10. Show output count: `output`
11. Display output help screen: `output help`
12. Add an output to an endpoint: `output add X` where `X` is connection string.
    1. Connection strings are covered before in [here](mavproxy-quickstart.md).
13. List existing outputs: `output list`
14. Remove an output using: `output remove X` where `X` is the output index.

[Source](https://ardupilot.org/mavproxy/docs/modules/link.html)