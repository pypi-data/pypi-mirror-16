# aiopype

Python asynchronous data pipelines

**aiopype** allows running continuous data pipelines reliably with a plain simple approach to their development.

**Aiopype** creates a centralized message handler to allow every processor to work as an independent non-blocking message producer/consumer.

**Aiopype** has 4 main concepts:

- Flow
- Manager
- Processor
- Message Handler

## Flow

The Flow is **aiopype**'s main component. A flow is the entrypoint for reliability running pipeline managers.

`Flow` is responsible for:

- Starting all registered managers
- Handling manager failures
- Reporting errors
- Restarting failed managers

## Manager

The manager is responsible for registering a data pipeline from top to bottom. This means it must register a source and connect it with it's consumers, until the pipeline finally outputs.

## Processor

A processor is a message consumer/producer.

### Sources

Sources are special cases of processors. Their special characteristic is that they can run forever, and are the starting point of any pipeline.  

Examples of sources may be:

- A `REST API` poller
- An `Websocket` client
- A `Cron` job

## Message handler

The message handler is the central piece that allows **aiopype** to scale.

A Flow will start one or more Sources as the starting point for each registered Manager. Once a Source produces an event, a message will be triggered and the handler will identify and fire the corresponding handlers.

There are two available message handlers:

- SyncProtocol
- AsyncProtocol

## SyncProtocol

The synchronous event handler is, as its name suggests, synchronous, meaning that once the source emits a message, it must be handled until the end of the pipeline and the source can proceed with it's normal behavior. This is good for development purposes but fails to meet the asynchronous event driven pattern required to allowing component isolation.

## AsyncProtocol

The main difference between SyncProtocol and AsyncProtocol is that the latter uses a decoupled event loop to assess if there are new messages in the queue for processing, whilst the first simply starts processing received messages instantaneously. This allows total isolation of processors.

# Example

Apple stock processor.

## Source

Our source will be `Yahoo Finance` for gathering data from `AAPL` ticker price. We'll use **aiopype** `RestSource` as a base class.

```py
from aiopype.sources import RestSource


class YahooRestSource(RestSource):
  """
  Yahoo REST API source.
  """
  def __init__(self, name, handler, symbol):
    super().__init__(
      name,
      handler,
      'http://finance.yahoo.com/webservice/v1/symbols/{}/quote?format=json&view=detail'.format(symbol), {
        'exception_threshold': 10,
        'request_interval': 30
      }
    )
```

## Processor

Our sample processor will simply extract the price from the returned json.

```py
from aiopype import Processor


class HandleRawData(Processor):
  def handle(self, data, time):
    self.emit('price', time, data['list']['resources'][0]['resource']['fields']['price'])
```

## Output

Our output processor will write price data onto a CSV File.

```py
import csv


class CSVOutput(Processor):
  def __init__(self, name, handler, filename):
    super().__init__(name, handler)
    self.filename = filename

    with open(self.filename, 'w', newline = '') as csvfile:
      writer = csv.writer(csvfile, delimiter = ';')
      writer.writerow(['time', 'price'])

  def write(self, time, price):
    with open(self.filename, 'w', newline = '') as csvfile:
      writer = csv.writer(csvfile, delimiter = ';')
      writer.writerow([time, price])
```

## Manager

The manager will instantiate `Source`, `Processor` and `Output`. It will connect `Source`'s `data` event to `Processor.handle` handler and `Processor`'s `price` event to `Output.write` handler. This will be our data pipeline.

```py
from aiopype import Manager


class YahooManager(Manager):
  name = 'yahoo_apple'

  def __init__(self, handler):
    super().__init__(handler)
    self.processor = HandleRawData(self.build_processor_name('processor'), self.handler)
    self.source = YahooRestSource(self.build_processor_name('source'), self.handler, 'AAPL')
    self.writer = CSVOutput(self.build_processor_name('writer'), self.handler, 'yahoo_appl.csv')

    self.source.on('data', self.processor.handle)
    self.processor.on('price', self.writer.write)
```

## Flow

Our flow config will have the `yahoo_apple` manager only.

```py
from aiopype import AsyncFlow


class FlowConfig(object):
  FLOWS = ['yahoo_apple']

dataflow = AsyncFlow(FlowConfig())
```

## Main method:

Will simply start the dataflow.

```py
if __name__ == "__main__":
  dataflow.start()
```

## Running the example

Compile all the above code in a file called `example.py` and run:

```sh
python example.py
```

# Clusters

## WIP:

This decentralized mechanism makes distributed pipelines a possibility, if we have coordination between nodes.
