#include <stdio.h>
#include <pb_encode.h>
#include <pb_decode.h>
#include "sdp.pb.h"

int main()
{
    /* This is the buffer where we will store our message. */
    uint8_t buffer[Message_size];
    size_t message_length;
    bool status;

    /* Encode our message */
    {
        /* Allocate space on the stack to store the message data.
         *
         * Nanopb generates simple struct definitions for all the messages.
         * - check out the contents of simple.pb.h! */
        Message message = Message_init_zero;

        /* Create a stream that will write to our buffer. */
        pb_ostream_t stream = pb_ostream_from_buffer(buffer, sizeof(buffer));

        /* Fill in the MSG Type */
        message.msg_type = MSG_REQ_LOGIN;
		printf("%d, %d\n", MSG_REQ_LOGIN, sizeof(Message));
        /* Now we are ready to encode the message! */
        status = pb_encode(&stream, Message_fields, &message);
		printf("%d\n", status);
        message_length = stream.bytes_written;
		printf("msg_len = %d\n", stream.bytes_written);

        /* Then just check for any errors.. */
        if (!status)
        {
            printf("Encoding failed: %s\n", PB_GET_ERROR(&stream));
            return 1;
        }
    }

    /* Now we could transmit the message over network, store it in a file or
     * wrap it to a pigeon's leg.
     */

    /* But because we are lazy, we will just decode it immediately. */

    {
        /* Allocate space for the decoded message. */
        Message message;

        /* Create a stream that reads from the buffer. */
        pb_istream_t stream = pb_istream_from_buffer(buffer, message_length);

        /* Now we are ready to decode the message. */
        status = pb_decode(&stream, Message_fields, &message);

        /* Check for errors... */
        if (!status)
        {
            printf("Decoding failed: %s\n", PB_GET_ERROR(&stream));
            return 1;
        }

        /* Print the data contained in the message. */
        printf("Your msg type was %d!\n", message.msg_type);
    }

    return 0;
}
